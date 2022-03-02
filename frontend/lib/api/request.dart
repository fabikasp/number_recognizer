import 'package:http/http.dart';

class Request {
  static const String URL = 'http://10.0.2.2:5000/';

  static Future evaluateNumberOnPicture(encodedImageBytes) async {
    Response response = await post(
      URL,
      body: {'encodedImageBytes': encodedImageBytes}
    );

    return response.body;
  }
}