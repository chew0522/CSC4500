import 'package:flutter/material.dart';
import 'package:frontend/DetectPage.dart';
import 'package:frontend/HomePage.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/',
      routes:{
        '/': (context) => HomePage(),
        '/DetectPage': (context) => DetectPage(),
      }
    );
  }
}