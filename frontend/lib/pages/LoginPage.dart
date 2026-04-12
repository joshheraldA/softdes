import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:frontend/widget_bundles/LoginWidget.dart';
import 'package:frontend/widget_bundles/RegisterWidget.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  int _currentPage = 1;

  @override
  Widget build(BuildContext context) {
    final pages = [
      LoginWidget(onSwitchToRegister: () => setState(() => _currentPage = 1)),
      RegisterWidget(onSwitchToLogin: () => setState(() => _currentPage =0)),
    ];

    return Scaffold(
      body: Stack(
        children: [
          // Layer 1: The Image
          Container(
            decoration: const BoxDecoration(
              image: DecorationImage(
                image: AssetImage('assets/login_background.jpg'),
                fit: BoxFit.cover,
              ),
            ),
          ),
          // Layer 2: The Blur Filter
          BackdropFilter(
            filter: ImageFilter.blur(sigmaX: 10.0, sigmaY: 10.0),
            child: Container(
              color: const Color.fromARGB(255, 0, 0, 0).withValues(alpha: 0.1),
            ), // Optional: darkens the bg slightly
          ),
          // Layer 3: Your Widgets
          SafeArea(child: pages[_currentPage]),
        ],
      ),
    );
  }
}
