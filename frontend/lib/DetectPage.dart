import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class DetectPage extends StatefulWidget {
  @override
  DetectPageState createState() => DetectPageState();
}

class DetectPageState extends State<DetectPage> {
  final TextEditingController subjectController = TextEditingController();
  final TextEditingController contentController = TextEditingController();
  String emailPrediction = '';
  String urlPrediction = '';

  Future<void> checkPhishing() async {
    final url = Uri.parse('http://10.0.2.2:5000/predict');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'subject': subjectController.text,
        'content': contentController.text,
      }),
    );

    if (response.statusCode == 200) {
      final result = json.decode(response.body);
      setState(() {
        emailPrediction = result['email_prediction'];
        urlPrediction = result['url_prediction'];
      });
    } else {
      setState(() {
        emailPrediction = 'Error: ${response.statusCode}';
        urlPrediction = 'Error: ${response.statusCode}';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    const Color primaryColor = Color.fromARGB(255, 52, 73, 94);

    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back, color: Colors.white),
          onPressed: () => Navigator.pop(context),
        ),
        title: const Text(
          'Phishing Email Detector',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: primaryColor,
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Enter Email Details:',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: primaryColor,
                ),
              ),
              const SizedBox(height: 15),

              // Subject Input
              TextField(
                controller: subjectController,
                decoration: InputDecoration(
                  labelText: 'Email Subject',
                  border: OutlineInputBorder(),
                  focusedBorder: OutlineInputBorder(
                    borderSide: BorderSide(color: primaryColor),
                  ),
                ),
              ),
              const SizedBox(height: 15),

              // Content Input
              TextField(
                controller: contentController,
                maxLines: 5,
                decoration: InputDecoration(
                  labelText: 'Email Content',
                  border: OutlineInputBorder(),
                  focusedBorder: OutlineInputBorder(
                    borderSide: BorderSide(color: primaryColor),
                  ),
                ),
              ),
              const SizedBox(height: 25),

              // Check Button
              Center(
                child: ElevatedButton(
                  onPressed: checkPhishing,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: primaryColor,
                    padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 15),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                  child: const Text(
                    'Check for Phishing',
                    style: TextStyle(fontSize: 16, color: Colors.white),
                  ),
                ),
              ),

              const SizedBox(height: 30),

              // Results
              if (emailPrediction.isNotEmpty || urlPrediction.isNotEmpty)
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: primaryColor.withOpacity(0.1),
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(color: primaryColor),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Email Prediction: $emailPrediction',
                        style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: primaryColor),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        'URL Prediction: $urlPrediction',
                        style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: primaryColor),
                      ),
                    ],
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
