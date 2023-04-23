const int buttonPin = 2; // ボタンが接続されたピン
const int debounceDelay = 100; // チャタリング防止用の待ち時間（ミリ秒）
int current = 0;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // ピンを入力モードに設定
  Serial.begin(9600); // シリアル通信を開始
}

void loop() {
  int buttonState = digitalRead(buttonPin); // ボタンの状態を読み取る
  if (buttonState == LOW) { // ボタンが押されたら
    if (current == 1){
      
    }
    else{
      current = 1;
      Serial.println("click"); // シリアル通信で"click"と送信する（改行なし）
      delay(debounceDelay); // チャタリング防止用に少し待つ
    }
    
  }
  if (buttonState == HIGH) {
    if (current == 1){
      Serial.println("done");
      current = 0;
      delay(debounceDelay); // チャタリング防止用に少し待つ
    }
    
  }
}