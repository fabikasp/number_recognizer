import 'dart:convert';
import 'dart:io';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:numberrecognizer/api/request.dart';
import 'package:numberrecognizer/screens/NumberRecognizerScreen/widgets/EvaluationBox.dart';
import 'package:numberrecognizer/screens/NumberRecognizerScreen/widgets/RepeatButton.dart';
import 'package:numberrecognizer/screens/NumberRecognizerScreen/widgets/ImageStorageSpace.dart';

class NumberRecognizerScreen extends StatefulWidget {
  @override
  _NumberRecognizerScreenState createState() => _NumberRecognizerScreenState();
}

class _NumberRecognizerScreenState extends State<NumberRecognizerScreen> {
  File image;
  String evaluationText;
  bool numberRecognized = false;

  void selectAndEvaluatePicture() async {
    File image = await ImagePicker.pickImage(source: ImageSource.gallery);
    List<int> imageBytes = image.readAsBytesSync();

    String resultNumberData = await Request.evaluateNumberOnPicture(base64Encode(imageBytes));
    int resultNumber = jsonDecode(resultNumberData)['resultNumber'] ?? null;

    setState(() {
      this.image = image;

      if (resultNumber != null) {
        this.numberRecognized = true;
        this.evaluationText = 'Nummer erkannt: ' + resultNumber.toString();
      } else {
        this.numberRecognized = false;
        this.evaluationText = 'Keine Nummer erkannt';
      }
    });
  }

  Widget loadImage() {
    if (this.image != null) {
      return Image.file(
        this.image,
        width: 300.0,
        height: 300.0,
        fit: BoxFit.fitHeight
      );
    }

    return ImageStorageSpace(this.selectAndEvaluatePicture);
  }

  Widget loadEvaluationArea() {
    if (this.evaluationText != null) {
      return Center(
        child: Column(
          children: <Widget>[
            SizedBox(height: 20),
            EvaluationBox(this.numberRecognized, this.evaluationText),
            SizedBox(height: 15),
            RepeatButton(this.selectAndEvaluatePicture),
          ],
        ),
      );
    }

    return Container();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
          child: AppBar(
            title: Column(
              children: <Widget>[
                SizedBox(height: 32),
                Text(
                  'NumberRecognizer',
                  style: TextStyle(
                    color: Colors.white,
                    fontFamily: 'Roboto',
                    fontWeight: FontWeight.bold,
                    fontSize: 22
                  ),
                ),
              ],
            ),
            centerTitle: true,
            backgroundColor: Colors.blueGrey,
        ),
        preferredSize: Size.fromHeight(75)
      ),
      body: Container(
        child: Center(
          child: Column(
            children: <Widget>[
              this.loadImage(),
              this.loadEvaluationArea(),
            ],
            mainAxisAlignment: MainAxisAlignment.center,
          )
        ),
      ),
    );
  }
}
