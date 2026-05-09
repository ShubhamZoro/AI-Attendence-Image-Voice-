# 📸 SnapClass — AI-Powered Attendance System

> **Making attendance faster using AI** — a multi-modal attendance system that uses **Face Recognition** and **Voice Recognition** to automatically mark student attendance.

🌐 **Live Demo**: [snapclass-attendance-img-voice.streamlit.app](https://snapclass-attendance-img-voice.streamlit.app)

---

## ✨ Features

### 👨‍🏫 For Teachers
- 🔐 Secure login & registration with bcrypt-hashed passwords
- 📚 Create and manage subjects with unique subject codes
- 📷 **Image-based attendance** — upload a class photo to auto-detect & mark present students
- 🎙️ **Voice-based attendance** — upload a bulk audio file; voices are matched to enrolled students
- 📊 View detailed **attendance records** per subject with timestamps
- 🔗 **Share class links** via QR code or copy-paste URL for students to self-enroll

### 👨‍🎓 For Students
- 🔐 Student login & registration
- 📸 Add face photo for face recognition enrollment
- 🎤 Add voice sample for voice recognition enrollment
- 📚 Enroll in subjects via subject code or scanned QR code link
- 📈 View personal attendance stats per subject (present / total)
- 🚪 Unenroll from any subject

---

## 🧠 AI / ML Architecture

### Face Recognition Pipeline (`src/pipelines/face_pipeline.py`)
| Step | Technology |
|------|-----------|
| Face Detection | `dlib` frontal face detector |
| Landmark Prediction | `dlib` 68-point shape predictor |
| Embedding Extraction | `dlib` ResNet face recognition model (128-d) |
| Classification | `scikit-learn` SVM (linear kernel, probability-calibrated) |
| Threshold | Euclidean distance ≤ 0.6 |

### Voice Recognition Pipeline (`src/pipelines/voice_pipeline.py`)
| Step | Technology |
|------|-----------|
| Audio Loading | `librosa` (resampled to 16 kHz) |
| Preprocessing | `resemblyzer.preprocess_wav` |
| Embedding Extraction | `resemblyzer` VoiceEncoder (256-d d-vector) |
| Speaker Identification | Cosine similarity with threshold 0.65 |
| Bulk Audio Segmentation | `librosa.effects.split` (top_db=30, min 0.5s segments) |

---

## 🗄️ Database Schema (Supabase / PostgreSQL)

```
teachers          students
─────────         ─────────
teacher_id  ◄──┐  student_id
username        │  name
password        │  face_embedding  (JSONB)
name            │  voice_embedding (JSONB)
                │
subjects        │  subject_students (junction)
─────────       │  ──────────────────
subject_id      │  subject_id ──► subjects
subject_code    │  student_id ──► students
name            │
section         │
teacher_id ─────┘

attendance_logs
───────────────
id
timestamp
subject_id ──► subjects
student_id ──► students
is_present
```

> Run `supabase.sql` to initialize all tables in your Supabase project.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A [Supabase](https://supabase.com) project
- `cmake` and C++ build tools (required by `dlib`)

### 1. Clone the Repository
```bash
git clone https://github.com/ShubhamZoro/AI-Attendence-Image-Voice-.git
cd AI-Attendence-Image-Voice-
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> ⚠️ `dlib-bin` and `face_recognition_models` may take a few minutes to install.

### 3. Set Up Supabase
1. Create a new project at [supabase.com](https://supabase.com)
2. Open the **SQL Editor** and run the contents of `supabase.sql`
3. Copy your **Project URL** and **anon key** from Project Settings → API

### 4. Configure Secrets
Create `.streamlit/secrets.toml`:
```toml
SUPABASE_URL = "https://your-project-id.supabase.co"
SUPABASE_ANON_KEY = "your-anon-key-here"
```

### 5. Run the App
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📁 Project Structure

```
AI Attendence/
├── app.py                        # App entry point & routing
├── requirements.txt              # Python dependencies
├── supabase.sql                  # Database schema
├── .streamlit/
│   └── secrets.toml              # API keys (not committed)
└── src/
    ├── screens/
    │   ├── home_screen.py        # Landing / login selector
    │   ├── teacher_screen.py     # Teacher dashboard
    │   └── student_screen.py     # Student dashboard
    ├── pipelines/
    │   ├── face_pipeline.py      # Face detection, embedding & SVM classifier
    │   └── voice_pipeline.py     # Voice embedding & speaker identification
    ├── components/
    │   ├── dialog_add_photo.py        # Student photo upload dialog
    │   ├── dialog_voice_attendance.py # Voice attendance dialog
    │   ├── dialog_attendance_results.py # Results display dialog
    │   ├── dialog_create_subject.py   # Create subject dialog
    │   ├── dialog_share_subject.py    # QR code share dialog
    │   ├── dialog_enroll.py           # Manual enroll dialog
    │   ├── dialog_auto_enroll.py      # Auto-enroll via URL join code
    │   ├── subject_card.py            # Subject card UI component
    │   ├── header.py                  # Dashboard header
    │   └── footer.py                  # App footer
    ├── database/
    │   └── db.py                 # All Supabase CRUD operations
    └── ui/
        └── base_layout.py        # Global styles & layout helpers
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select your repository and set **Main file** to `app.py`
4. Under **Advanced settings → Secrets**, paste:
   ```toml
   SUPABASE_URL = "https://your-project-id.supabase.co"
   SUPABASE_ANON_KEY = "your-anon-key-here"
   ```
5. Click **Deploy**

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Frontend / App | Streamlit |
| Face Detection | dlib |
| Face Recognition | face_recognition_models (ResNet) |
| Voice Recognition | resemblyzer |
| Audio Processing | librosa |
| ML Classifier | scikit-learn (SVM) |
| Database | Supabase (PostgreSQL) |
| Auth | bcrypt |
| QR Code | segno |
| Image Processing | Pillow, NumPy |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Built with ❤️ using Streamlit & AI</p>
