# Gesture-Login 🖐️

A gesture-based authentication system that recognizes hand gestures for secure login verification.

## Features

- 🎥 Real-time hand gesture recognition using computer vision
- 🔐 Gesture-based authentication (V-sign gesture for login)
- 📱 Uses MediaPipe for hand landmark detection
- ⚡ Fast and responsive recognition
- 🎯 High accuracy hand tracking

## Requirements

- Python 3.8 or higher
- Webcam/Camera device

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/EltunLTN/Gesture-Login.git
cd Gesture-Login
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Dependencies

The project requires:
- **tensorflow==2.13.0** - Machine learning framework
- **opencv-python** - Computer vision library
- **opencv-contrib-python** - OpenCV contrib modules
- **numpy** - Numerical computing
- **mediapipe==0.10.5** - Hand gesture recognition
- **protobuf>=5.28.0** - Protocol buffer library

## Usage

Run the login script:

```bash
python login.py
```

### How it works:

1. The program opens your webcam
2. A message displays: "Giriş üçün əl jestini göstərin (✌️):" (Show hand gesture for login)
3. Show the **V-sign gesture** (✌️) - index and middle fingers extended, other fingers closed
4. The system recognizes the gesture and grants access
5. If the gesture doesn't match, access is denied

## Files

- `login.py` - Main login script
- `gesture_recognizer.py` - Hand gesture recognition module
- `train_model.py` - Model training script
- `verify_gesture.py` - Gesture verification utility
- `requirements.txt` - Project dependencies

## Gesture Recognition

The system currently recognizes the following gesture:

| Gesture | Description | Status |
|---------|-------------|--------|
| V-sign (✌️) | Index and middle fingers up, others down | Active |

## Troubleshooting

### ImportError: cannot import name 'solutions' from 'mediapipe'
- **Solution:** Update dependencies using the provided requirements.txt
```bash
pip install -r requirements.txt
```

### Camera not recognized
- Ensure your camera is connected and working
- Check camera permissions in your system settings
- Try restarting the application

### Performance issues
- Ensure your camera resolution is not too high (720p-1080p recommended)
- Close other applications using the camera
- Check CPU usage during execution

## Development

To extend gesture recognition:

1. Edit `gesture_recognizer.py` to add new gesture patterns
2. Update the `fingers_up()` function to recognize additional gestures
3. Add corresponding gesture logic in the main login function

## License

This project is open source and available under the MIT License.

## Author

**EltunLTN** - [GitHub Profile](https://github.com/EltunLTN)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Future Enhancements

- [ ] Add more gesture recognition patterns
- [ ] Implement gesture recording and training
- [ ] Add user profile management
- [ ] Implement gesture combinations
- [ ] Add UI improvements
- [ ] Deploy as web application

---

**Last Updated:** February 1, 2026
