import 'package:flutter/material.dart';

class RepeatButton extends StatelessWidget {
  final Function selectAndEvaluatePicture;

  RepeatButton(this.selectAndEvaluatePicture);

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => this.selectAndEvaluatePicture(),
      child: Center(
        child: Container(
          decoration: BoxDecoration(color: Colors.blueGrey),
          width: 172,
          height: 50,
          child: Row(
            children: <Widget>[
              Icon(
                Icons.refresh,
                size: 35,
                color: Colors.white,
              ),
              SizedBox(width: 5),
              Text(
                'Wiederholen',
                style: TextStyle(
                  color: Colors.white,
                  fontFamily: 'Roboto',
                  fontWeight: FontWeight.bold,
                  fontSize: 22
                ),
              ),
            ],
          ),
        ),
      )
    );
  }
}
