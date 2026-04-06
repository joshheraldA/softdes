import 'package:flutter/material.dart';

class FancyHeader extends StatelessWidget {
  final String UserText;
  const FancyHeader({super.key, required this.UserText});

  @override
  Widget build(BuildContext context) {
    return Text(
      UserText,
      style: TextStyle(fontFamily: 'sans-serif', fontSize: 50),
    );
  }
}
