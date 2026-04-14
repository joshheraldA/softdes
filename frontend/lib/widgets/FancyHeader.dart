import 'package:flutter/material.dart';

class FancyHeader extends StatelessWidget {
  final String userText;
  final double textSize;
  final String familyFont;
  final int weightFont;

  const FancyHeader({
    super.key, 
    required this.userText,
    this.familyFont = 'sans-serif',
    this.weightFont = 50,
    this.textSize = 50,
  });

  @override
  Widget build(BuildContext context) {
    return Text(
      userText,
      style: TextStyle(
        fontFamily: 'sans-serif', 
        fontWeight: FontWeight(weightFont),
        fontSize: textSize
        ),
    );
  }
}
