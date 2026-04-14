import 'package:flutter/material.dart';
import 'package:frontend/pages/HomePage.dart';
import 'package:frontend/widgets/FancyButton.dart';

class AccountPage extends StatelessWidget {
  const AccountPage({super.key});

  @override
  Widget build(BuildContext context) {

  void go_back() {

    Navigator.pushReplacement(
      context, 
      MaterialPageRoute(builder: (_) => HomePage(
        username: "woshy", 
        cesPoints: 0)
      ));
  }
    return Scaffold(
      appBar: AppBar(
        title: Text("User account"),
      ),
      body: Center(
        child: Container(
          color: Colors.red,
          child: FancyButton(
            function: () => {
              go_back()
            }, 
            text: "SENPAI")
        ),
      )
    );
  }
}
