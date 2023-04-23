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
        appBar: AppBar(title: Text('Endpoint Challenge')),
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

  Future<void> _getEncryptedSecret() async {
    final response = await http.get(
      Uri.parse('http://russian-bot.net:5050/token'),
      headers: {'x-api-key': 'not_the_api_key'},
    );

    if (response.statusCode == 200) {
      setState(() {
        _result = jsonDecode(response.body)['encrypted_secret'];
      });
    } else {
      setState(() {
        _result = 'Error: Could not retrieve encrypted secret';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        ElevatedButton(
          onPressed: _getEncryptedSecret,
          child: Text('Retrieve Encrypted Secret'),
        ),
        SizedBox(height: 20),
        if (_result != null) Text(_result!),
      ],
    );
  }
}
