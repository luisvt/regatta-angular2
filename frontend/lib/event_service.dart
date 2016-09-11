import 'dart:async';
import 'dart:convert';

import 'package:angular2/core.dart';
import 'package:http/http.dart';

import 'event.dart';


@Injectable()
class EventService {

  static const _eventsUrl = 'http://localhost:8000/api/events/'; // URL to web API

  final Client _http;

  EventService(this._http);

  Future<List<Event>> getEvents() async {
    try {
      final response = await _http.get(_eventsUrl);
      final events = _extractData(response)
          .map((value) => new Event.fromJson(value))
          .toList();
      return events;
    } catch (e) {
      throw _handleError(e);
    }
  }

  Future<Event> getEvent(int id) async {
    try {
      final response = await _http.get(_eventsUrl + id.toString());
      final event = new Event.fromJson(JSON.decode(response.body));
      return event;
    } catch (e) {
      throw _handleError(e);
    }
  }

  dynamic _extractData(Response resp) => JSON.decode(resp.body)['results'];

  Exception _handleError(dynamic e) {
    print(e); // for demo purposes only
    return new Exception('Server error; cause: $e');
  }

}
