

import 'package:flutter/material.dart';
import 'package:frontend/widget_bundles/LoginWidget.dart';
import 'package:frontend/widget_bundles/RegisterWidget.dart';
class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  int _currentPage = 0;

  @override
  Widget build(BuildContext context) {
    final pages = [
      LoginWidget(onSwitchToRegister: () => setState(() => _currentPage = 1)),
      RegisterWidget(onSwitchToLogin: () => setState(() => _currentPage = 0)),
    ];

    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage('assets/login_background.jpg'),
            fit: BoxFit.fill,
          ),
        ),
        child: pages[_currentPage],
      ),
    );
  }
}