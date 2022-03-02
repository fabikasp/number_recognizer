import 'package:flutter/material.dart';

class EvaluationBox extends StatelessWidget {
  final bool numberRecognized;
  final String evaluationText;

  EvaluationBox(this.numberRecognized, this.evaluationText);

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(color: Colors.grey),
      width: this.numberRecognized ? 250 : 280,
      height: 40,
      child: Row(
        children: <Widget>[
          Icon(
            this.numberRecognized
              ? Icons.check_circle_outline
              : Icons.error_outline,
            size: 35,
            color: Colors.white,
          ),
          SizedBox(width: 5),
          Text(
            this.evaluationText,
            style: TextStyle(
              color: Colors.white,
              fontFamily: 'Roboto',
              fontWeight: FontWeight.bold,
              fontSize: 22
            ),
          ),
        ],
        mainAxisAlignment: MainAxisAlignment.center,
      ),
    );
  }
}
