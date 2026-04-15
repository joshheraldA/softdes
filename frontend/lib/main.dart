import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:frontend/firebase_options.dart';
// import 'package:frontend/pages/HomePage.dart';
import 'package:frontend/pages/LoginPage.dart';
// import 'package:frontend/pages/LoginPage.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
    colorScheme: ColorScheme.fromSeed(seedColor: const Color.fromARGB(255, 153, 194, 228)),
    useMaterial3: true,
  ),
      debugShowCheckedModeBanner: false,
      // home: HomePage(username: "joshywoshy", cesPoints: 0),
      home: LoginPage()
    );
  }
}