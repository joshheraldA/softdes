import 'package:flutter/material.dart';
import 'package:frontend/firebase/FbAuth.dart';
import 'package:frontend/pages/LoginPage.dart';
import 'package:frontend/pages/account.dart';
import 'package:frontend/widgets/ActionCard.dart';
import 'package:frontend/widgets/FancyHeader.dart';
// import 'package:frontend/widgets/FancyButton.dart';

class HomePage extends StatefulWidget {
  final String username;
  final int cesPoints;
  const HomePage({super.key, required this.username, required this.cesPoints});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late double percentage; 

  @override
  void initState() {
    super.initState();
    percentage = (widget.cesPoints / 60).clamp(0, 1);
    
  }

  void handleLogout() {
    signOut();

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(builder: (_) => LoginPage()),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        leading: Container(
          margin: EdgeInsets.fromLTRB(20, 0, 0, 0),
          alignment: Alignment.centerLeft,
          child: FancyHeader(userText: "CES APP", textSize: 25,),
        ),
        leadingWidth: (MediaQuery.of(context).size.width * 0.1),
        elevation: 2.0, // Increase for more prominent shadow
// Instead of the deprecated .withOpacity(0.5)
          shadowColor: Colors.black.withValues(alpha: 0.5),       
          actions: <Widget>[
          Padding(
            padding: EdgeInsetsGeometry.all(5),
            child: GestureDetector(
            onTap: () => {
              Navigator.pushReplacement(
                context, 
                MaterialPageRoute(builder: (_) => AccountPage()))
            },
            child: Image.network("https://cdn-icons-png.flaticon.com/512/8345/8345328.png")
            ),
          ),
        ],
        
      ),
      body: Column(
        children: [
          Row(
            children: [
              ActionCard(
                heightVal:  MediaQuery.of(context).size.height * 0.3, 
                widthVal: MediaQuery.of(context).size.width * 0.15, 
                childWidg: CircularProgressIndicator(
                  value: percentage, // 70% progress
                  backgroundColor: const Color.fromARGB(255, 244, 244, 244),
                  valueColor: AlwaysStoppedAnimation<Color>(const Color.fromARGB(255, 235, 192, 127)),
                  strokeWidth: 5.0,                 
                ),
                bgColor: const Color.fromARGB(255, 243, 243, 243),
              ),
            ],
          )
        ],
      ),

      // body: Center(
      //   child: Column(
      //     children: [
      //       Text("Logged in!"),
      //       Text("Username: ${widget.username}"),
      //       Text("Ces Points: ${widget.cesPoints}"),
      //       FancyButton(
      //         function: handleLogout,
      //         text: "Log out",
      //         buttonColor: Colors.redAccent,
      //         textColor: Colors.white,
      //       ),
      //     ],
      //   ),
      // ),
    );
  }
}
