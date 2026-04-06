import 'package:flutter/material.dart';
import 'package:frontend/firebase/FbAuth.dart';
import 'package:frontend/widgets/FancyButton.dart';
import 'package:frontend/widgets/FancyHeader.dart';
import 'package:frontend/widgets/FancyTextField.dart';

class RegisterWidget extends StatefulWidget {
  final VoidCallback onSwitchToLogin;

  const RegisterWidget({super.key, required this.onSwitchToLogin});

  @override
  State<RegisterWidget> createState() => _RegisterWidgetState();
}

class _RegisterWidgetState extends State<RegisterWidget> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Center(
      child: SizedBox(
        width: MediaQuery.of(context).size.width * 0.5,
        height: MediaQuery.of(context).size.height * 0.6,
        child: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(3),
            color: const Color.fromARGB(255, 255, 255, 255),
            boxShadow: [
              BoxShadow(
                color: const Color.fromARGB(99, 188, 188, 188),
                blurRadius: .2,
                offset: Offset(1, 1),
                spreadRadius: 1.0,
              ),
            ],
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              FancyHeader(UserText: 'Register'),
              Container(
                padding: EdgeInsets.all(8),
                width: MediaQuery.of(context).size.width * 0.2,
                height: MediaQuery.of(context).size.height * 0.06,
                child: FancyTextField(
                  hint: 'Enter email',
                  label: 'Email',
                  controller: emailController,
                ),
              ),
              Container(
                padding: EdgeInsets.all(8),
                width: MediaQuery.of(context).size.width * 0.2,
                height: MediaQuery.of(context).size.height * 0.06,
                child: FancyTextField(
                  hint: 'Enter Password',
                  label: 'Password',
                  controller: passwordController,
                  obscureText: true,
                ),
              ),

              Container(
                width: MediaQuery.of(context).size.width * 0.2,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Forgot your password?',
                      style: TextStyle(
                        color: const Color.fromARGB(255, 147, 147, 147),
                      ),
                    ),
                    TextButton(
                      child: Text(
                        'Sign in',
                        style: TextStyle(
                          color: const Color.fromARGB(255, 147, 147, 147),
                        ),
                      ),
                      onPressed: (){
                        setState(() {
                          widget.onSwitchToLogin();
                        });
                        
                      },
                    ),
                  ],
                ),
              ),
              FancyButton(
                function: () {
                  register(emailController.text, passwordController.text);
                  emailController.clear();
                  passwordController.clear();

                  
                },
                text: 'Register',
              ),
            ],
          ),
        ),
      ),
    );
  }
}
