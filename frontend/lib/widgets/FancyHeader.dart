import 'package:flutter/material.dart';

class FancyHeader extends StatelessWidget {
  final String userText;
  final double textSize;
  const FancyHeader({super.key, required this.userText, this.textSize = 50});

  @override
  Widget build(BuildContext context) {
    return Text(
      userText,
      style: TextStyle(fontFamily: 'sans-serif', fontSize: textSize),
    );
  }
}
