import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Bad Oauth')),
        body: Center(child: ChallengeWidget()),
      ),
    );
  }
}

class ChallengeWidget extends StatefulWidget {
  @override
  _ChallengeWidgetState createState() => _ChallengeWidgetState();
}

class _ChallengeWidgetState extends State<ChallengeWidget> {
  String? _result;

  Future<void> _getPrivilegedData() async {
    String clientId = 'not_admin';
    // we removed the weak password
    // TODO Please update
    String clientSecret = '';

    final auth =
        'Basic ' + base64Encode(utf8.encode('$clientId:$clientSecret'));
    final tokenResponse = await http.post(
      Uri.parse('http://russian-bot.net:5000/token'),
      headers: {'Authorization': auth},
    );

    if (tokenResponse.statusCode == 200) {
      final accessToken = jsonDecode(tokenResponse.body)['access_token'];
      final dataResponse = await http.get(
        Uri.parse('http://russian-bot.net:5000/data'),
        headers: {'Authorization': 'Bearer $accessToken'},
      );

      if (dataResponse.statusCode == 200) {
        setState(() {
          _result = jsonDecode(dataResponse.body)['data'];
        });
      } else {
        setState(() {
          _result = 'Error: Could not retrieve privileged data';
        });
      }
    } else {
      setState(() {
        _result = 'Error: Invalid client credentials';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        ElevatedButton(
          onPressed: _getPrivilegedData,
          child: Text('Retrieve Privileged Data'),
        ),
        SizedBox(height: 20),
        if (_result != null) Text(_result!),
      ],
    );
  }
}
