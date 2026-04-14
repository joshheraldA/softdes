import 'package:flutter/material.dart';

class ActionCard extends StatefulWidget {
  final Color bgColor;
  final double widthVal, heightVal, borderRadiusVal;
  final Widget childWidg;

  const ActionCard({
    super.key, 
    required this.widthVal, 
    required this.heightVal, 
    required this.childWidg,
    this.bgColor = const Color.fromARGB(255, 165, 165, 165),
    this.borderRadiusVal = 10,
    });
  @override
  State<ActionCard> createState() => _ActionCardState();
}

class _ActionCardState extends State<ActionCard> {
  @override
  Widget build(BuildContext context) {
    return Container(
      width: widget.widthVal,
      height: widget.heightVal,
      decoration: BoxDecoration(
        color : widget.bgColor,
        borderRadius: BorderRadius.all(
          Radius.circular(
            widget.borderRadiusVal
            ),
          ),
      ),
      child: widget.childWidg,
    );
  }
}