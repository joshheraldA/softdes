import 'package:flutter/material.dart';

class FancyButton extends StatelessWidget {
  final VoidCallback function;
  final String text;
  final Color buttonColor;
  final Color textColor;
  const FancyButton({
    super.key,
    required this.function,
    required this.text,
    this.buttonColor = Colors.blue,
    this.textColor = Colors.white,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width * 0.1,
      height: MediaQuery.of(context).size.height * 0.06,
      padding: EdgeInsets.all(10),
      child: ElevatedButton(
        onPressed: function,
        child: Text(text, style: TextStyle(color: textColor)),
        style: ElevatedButton.styleFrom(
          backgroundColor: buttonColor,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.all(Radius.circular(5)),
          ),
        ),
      ),
    );
  }
}
