import 'package:flutter/material.dart';

class ImageStorageSpace extends StatelessWidget {
  final Function selectAndEvaluatePicture;

  ImageStorageSpace(this.selectAndEvaluatePicture);

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => this.selectAndEvaluatePicture(),
      child: Container(
        decoration: BoxDecoration(color: Colors.blueGrey),
        width: 300,
        height: 300,
        child: Icon(
          Icons.camera_alt,
          size: 50,
          color: Colors.white,
        ),
      ),
    );
  }
}
