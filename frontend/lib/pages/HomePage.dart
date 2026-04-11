import 'package:flutter/material.dart';
import 'package:frontend/firebase/FbAuth.dart';
import 'package:frontend/pages/LoginPage.dart';
import 'package:frontend/widgets/FancyButton.dart';

class HomePage extends StatefulWidget {
  final String username;
  final int cesPoints;
  const HomePage({super.key, required this.username, required this.cesPoints});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  void handleLogout() {
    signOut();

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(builder: (_) => LoginPage()),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          children: [
            Text("Logged in!"),
            Text("Username: ${widget.username}"),
            Text("Ces Points: ${widget.cesPoints}"),
            FancyButton(
              function: handleLogout,
              text: "Log out",
              buttonColor: Colors.redAccent,
              textColor: Colors.white,
            ),
          ],
        ),
      ),
    );
  }
}
