MedTrack is a small website where you keep a list of your medical products, like a glucose monitor or a painkiller, and manage them.

**What a person can do on it:**
- Sign up and log in with their own account
- Add a product: its name, whether it's a device or a drug, its status (draft, in review, approved), and what it's meant to be used for
- See all their products in a list, open one to see the details, edit it, or delete it
- Only see their *own* products. Another user can't view or touch yours.

**In plain terms:** it's a digital register or notebook for products. You log in, add things to it, change them, and remove them. That's all it does.

**Why we're building something this simple:** it's a learning project. It covers the basics almost every real Django app is built on: logging in, saving data in Postgres, and creating, reading, updating and deleting records (that's CRUD). Once that works, you'll know Django well enough to take on harder things.

It's also the first piece of the bigger project. Later we'll add regulatory documents to it, and AI agents (using ADK) that read a document and tell you how it affects your products. That's the part that's close to what Lexim does.