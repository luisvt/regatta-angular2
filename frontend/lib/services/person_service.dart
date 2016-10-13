import 'dart:async';
import 'dart:convert';
import 'package:angular2/angular2.dart';
import 'package:dson/dson.dart';
import 'package:frontend/models/person.dart';
import 'package:http/http.dart';


@Injectable()
class PersonService {

  PersonService(this._http);

  final Client _http;

  static final _headersGet = {'Accept': 'application/json'};
  static final _headersPost = {'Content-Type': 'application/json'};

  // Hostname in development mode points to Django port 8000, in production we set it to empty during pub build
  static const hostname = const String.fromEnvironment('hostname', defaultValue: 'http://localhost:8000');

  static const _personsUrl = hostname + '/api/persons';

  Future<Iterable<Person>> getAll([Map<String, dynamic> query]) async {
    try {
      final response = await _http.get('$_personsUrl/', headers: _headersGet);
      final results = JSON.decode(response.body)['results'];
      final persons = fromMapList(results, Person);
      return persons;
    } catch (e) {
      throw _handleError(e);
    }
  }

  Exception _handleError(dynamic e) {
    print(e); // for demo purposes only
    return new Exception('Server error; cause: $e');
  }

}