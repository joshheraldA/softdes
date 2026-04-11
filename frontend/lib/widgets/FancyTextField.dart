import 'package:flutter/material.dart';

class FancyTextField extends StatefulWidget {
  final String label;
  final String hint;
  final IconData? icon;
  final bool obscureText;
  final TextEditingController? controller;

  const FancyTextField({
    super.key,
    this.label = 'Label',
    this.hint = 'Enter text...',
    this.icon,
    this.controller,
    this.obscureText = false,
  });

  @override
  State<FancyTextField> createState() => _FancyTextFieldState();
}

class _FancyTextFieldState extends State<FancyTextField> {
  bool _isFocused = false;
  late bool _obscure;

  @override
  void initState() {
    super.initState();
    _obscure = widget.obscureText;
  }

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;

    return Focus(
      onFocusChange: (focused) => setState(() => _isFocused = focused),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(5),
          border: Border.all(
            color: _isFocused
                ? scheme.primary
                : scheme.outline.withOpacity(0.5),
            width: _isFocused ? 2 : 1,
          ),
          color: scheme.surfaceContainerLowest,
          boxShadow: _isFocused
              ? [
                  BoxShadow(
                    color: scheme.primary.withOpacity(0.12),
                    blurRadius: 8,
                  ),
                ]
              : [],
        ),
        child: TextField(
          controller: widget.controller,
          obscureText: _obscure,
          decoration: InputDecoration(
            // labelText: widget.label,
            hintText: widget.hint,
            prefixIcon: widget.icon != null
                ? Icon(widget.icon, size: 20)
                : null,
            suffixIcon: widget.obscureText
                ? IconButton(
                    icon: Icon(
                      _obscure ? Icons.visibility_off : Icons.visibility,
                      size: 20,
                    ),
                    onPressed: () => setState(() => _obscure = !_obscure),
                  )
                : null,
            border: InputBorder.none, // border handled by Container
            contentPadding: const EdgeInsets.symmetric(
              horizontal: 16,
              vertical: 12,
            ),
          ),
        ),
      ),
    );
  }
}
