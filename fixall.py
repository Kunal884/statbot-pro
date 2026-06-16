import os

folder = r"C:\Users\KUNAL GIRME\Downloads\statbot-master\statbot-master"

corrupted = []
for filename in os.listdir(folder):
    if filename.endswith(".py"):
        filepath = os.path.join(folder, filename)
        with open(filepath, "rb") as f:
            content = f.read()
        if b"\x00" in content:
            corrupted.append(filename)
            # Remove null bytes and save
            fixed = content.replace(b"\x00", b"")
            with open(filepath, "wb") as f:
                f.write(fixed)
            print(f"Fixed: {filename}")

if not corrupted:
    print("No corrupted files found!")
else:
    print(f"\nTotal fixed: {len(corrupted)} files")