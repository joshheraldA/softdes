import 'package:firebase_auth/firebase_auth.dart';

final auth = FirebaseAuth.instance;

Future<String?  > login_acc(String email, String password) async {

  /* 

    - you call the endpoint 
    - you get the data endpoint (insomnia is important because you don't know the name associated to the data)
    - you iterate through all the data 


  */ 
  try {
    UserCredential cred = await auth.signInWithEmailAndPassword(
      email: email,
      password: password,
    );
    print("Logged in: ${cred.user?.email}");
    return cred.user?.uid;
  } on FirebaseAuthException catch (e) {
    print("Error: ${e.message}");
    return null;
  }
}

Future<bool> register(String email, String password) async {
  try {
    UserCredential cred = await auth.createUserWithEmailAndPassword(
      email: email,
      password: password,
    );
    
    print("Registered: ${cred.user?.email}");
    return true;
  } on FirebaseAuthException catch (e) {
    print("Error: ${e.message}");
    return false;

  }
}

String? getUser(){
  User? user = auth.currentUser;
  if(user != null){
    return user.displayName;
  }
  return null;  
}

String? getEmail(){
   User? user = auth.currentUser;
  if(user != null){
    return user.email;
  }
  return null;  
}

void signOut() async {
  await auth.signOut();
}