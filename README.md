# 🌙 3AM Thoughts

A mysterious, endless-scrolling web application where the veil lifts for exactly one hour a day. Users can anonymously post their late-night thoughts, pictures, and videos—but the site is **only accessible between 3:00 AM and 4:00 AM local time**.

## Features
*   **Time-Gated Access**: A built-in JavaScript "vault door" constantly checks the visitor's local computer clock. It automatically snaps shut at 4:00 AM mid-scroll, and automatically fades away precisely at 3:00 AM without needing to refresh the page.
*   **Anonymous Posting**: No logins, no usernames. Just raw midnight thoughts.
*   **Media Support**: Users can upload images and videos directly to the feed.
*   **Sleek Aesthetic**: Built with a dark mode, glassmorphism design using Tailwind CSS.
*   **Vercel Ready**: Pre-configured with `vercel.json` and `requirements.txt` for fast deployment.

## Tech Stack
*   **Backend**: Django (Python)
*   **Database**: SQLite (Local Dev)
*   **Frontend**: HTML, JavaScript, Tailwind CSS (via CDN)

## How to Run Locally

1. **Activate the Virtual Environment**
   ```bash
   .\venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Database Migrations** (If you haven't already)
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the Server**
   ```bash
   python manage.py runserver
   ```
   *Visit `http://127.0.0.1:8000/` in your browser. (Note: If it isn't 3 AM, you will be locked out!)*

## Testing / Bypassing the Lock
If you are developing and need to see the feed when it's not 3 AM:
1. Open `mainapp/templates/mainapp/3am_feed.html`.
2. Scroll to the bottom JavaScript block.
3. Add `hour = 3;` right below `const hour = now.getHours();`.
4. Refresh your browser.

## Deployment Notes (Vercel)
This app is configured to be deployed on **Vercel** serverless functions. 
**Important Note:** Because Vercel has a read-only filesystem, SQLite will not permanently save new posts in production. To make this a fully functional public app where users can save data, you must switch the database in `settings.py` from SQLite to a Cloud PostgreSQL database (like Supabase, Neon, or Railway).
