# Naukri-Auto-Apply-Bot

🔍 **Naukri-Auto-Apply-Bot** is a Python-based automation tool that logs into your Naukri.com account, searches for jobs based on your criteria, and applies automatically to a specified number of jobs. This helps streamline the job application process and saves hours of manual work.

![Naukri Bot Demo](demo.gif)

> ✅ You can check the full [video demo here](https://github.com/visionEye0/Naukri-Auto-Apply-Bot/assets/your_video_link.mp4) (or see instructions below on how to embed).

---

## 🎯 Features

- Login automation via Naukri API
- Job search using:
  - Keywords
  - Location
  - Experience level
- Bulk auto-apply to jobs (default = 10)
- Progress bar and CLI feedback using `rich`
- Graceful error handling and summary output

---

## 🧑‍💻 How It Works

1. Authenticates your Naukri account using provided credentials
2. Searches for jobs matching your criteria
3. Automatically applies to a defined number of job listings
4. Displays a summary of successful and failed applications

---

## 📦 Dependencies

- `requests`
- `argparse`
- `asyncio`
- `rich`

Install them via:

```bash
pip install -r requirements.txt
```
## 🚀 Usage

```
python main.py -k "python developer, backend" -e 2 -l "Bangalore,Remote" -n 10 -u your-email@example.com -p your-password
```

### 🔧 Command-Line Options


| Option | Argument          | Description                                               | Required |
|--------|-------------------|-----------------------------------------------------------|----------|
| `-k`   | `[keywords]`       | Comma-separated job keywords (e.g., `"python,backend"`)   | ✅ Yes    |
| `-e`   | `[experience]`     | Job experience in years (e.g., `2`)                       | ❌ No     |
| `-l`   | `[location]`       | Job location(s), comma-separated (e.g., `"Remote,Bangalore"`) | ❌ No     |
| `-n`   | `[no of applies]`  | Number of job applications to send (default = 10)         | ❌ No     |
| `-u`   | `[username/email]` | Your Naukri account's email or username                   | ✅ Yes    |
| `-p`   | `[password]`       | Your Naukri account's password                            | ✅ Yes    |


📹 Demo

![Demo GIF](demo.gif)

## ⚠️ Disclaimer

This tool uses unofficial APIs and simulates job applications. Use at your own risk. Do not use with accounts you care about unless you're confident with the functionality.

## 📄 License

MIT License


## 🤝 Contributing

Pull requests and suggestions are welcome!