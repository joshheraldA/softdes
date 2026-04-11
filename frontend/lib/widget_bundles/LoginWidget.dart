import 'package:flutter/material.dart';
import 'package:frontend/firebase/FbAuth.dart';
import 'package:frontend/pages/HomePage.dart';
import 'package:frontend/widgets/FancyButton.dart';
import 'package:frontend/widgets/FancyHeader.dart';
import 'package:frontend/widgets/FancyTextField.dart';

class LoginWidget extends StatefulWidget {
  final VoidCallback onSwitchToRegister;

  const LoginWidget({super.key, required this.onSwitchToRegister});

  @override
  State<LoginWidget> createState() => _LoginWidgetState();
}

class _LoginWidgetState extends State<LoginWidget> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  bool confirm = false;
  bool _isLoading = false;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: SizedBox(
        width: MediaQuery.of(context).size.width * 0.5,
        height: MediaQuery.of(context).size.height * 0.6,
        child: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(20),
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
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              SizedBox(height: MediaQuery.of(context).size.height * 0.07),
              FancyHeader(userText: 'Login', textSize: 60),
              SizedBox(height: MediaQuery.of(context).size.height * 0.08),
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
                height:
                    MediaQuery.of(context).size.height *
                    0.06, // gets the size of the web browse
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
                        'Create an account',
                        style: TextStyle(
                          color: const Color.fromARGB(255, 147, 147, 147),
                        ),
                      ),
                      onPressed: () {
                        setState(() {
                          widget.onSwitchToRegister();
                        });
                      },
                    ),
                  ],
                ),
              ),

              _isLoading
                  ? CircularProgressIndicator()
                  : FancyButton(
                      function: () async {
                        setState(() => _isLoading = true);

                        confirm = await login(
                          emailController.text,
                          passwordController.text,
                        );

                        emailController.clear();
                        passwordController.clear();

                        setState(() => _isLoading = false);

                        if (confirm) {
                          Navigator.pushReplacement(
                            context,
                            MaterialPageRoute(builder: (_) => HomePage()),
                          );
                        }
                      },
                      text: 'Login',
                      buttonColor: Colors.green,
                    ),
            ],
          ),
        ),
      ),
    );
  }
}
