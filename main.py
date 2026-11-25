"""Track job applications locally with SQLite."""
import argparse, sqlite3
from datetime import date
from pathlib import Path
DB = Path(__file__).with_name("jobs.db")
STATUSES = ("saved", "applied", "interview", "offer", "rejected")

def db():
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    con.execute("""CREATE TABLE IF NOT EXISTS jobs(
        id INTEGER PRIMARY KEY, company TEXT NOT NULL, role TEXT NOT NULL,
        status TEXT NOT NULL, applied_on TEXT NOT NULL, follow_up TEXT, notes TEXT DEFAULT '')""")
    return con

def main():
    p=argparse.ArgumentParser(description="Track job applications.")
    s=p.add_subparsers(dest="cmd",required=True)
    a=s.add_parser("add"); a.add_argument("--company",required=True); a.add_argument("--role",required=True)
    a.add_argument("--status",choices=STATUSES,default="saved"); a.add_argument("--follow-up")
    a.add_argument("--notes",default="")
    u=s.add_parser("update"); u.add_argument("id",type=int); u.add_argument("--status",choices=STATUSES,required=True)
    s.add_parser("list"); s.add_parser("stats")
    x=p.parse_args()
    with db() as con:
        if x.cmd=="add":
            cur=con.execute("INSERT INTO jobs(company,role,status,applied_on,follow_up,notes) VALUES(?,?,?,?,?,?)",
                (x.company,x.role,x.status,date.today().isoformat(),x.follow_up,x.notes))
            print(f"Added application #{cur.lastrowid}.")
        elif x.cmd=="update":
            cur=con.execute("UPDATE jobs SET status=? WHERE id=?",(x.status,x.id))
            print("Updated." if cur.rowcount else "Application not found.")
        elif x.cmd=="list":
            rows=con.execute("SELECT * FROM jobs ORDER BY applied_on DESC,id DESC").fetchall()
            for r in rows: print(f"#{r['id']} | {r['company']} | {r['role']} | {r['status']} | follow-up: {r['follow_up'] or '-'}")
            if not rows: print("No applications yet.")
        else:
            for r in con.execute("SELECT status,COUNT(*) n FROM jobs GROUP BY status ORDER BY n DESC"):
                print(f"{r['status']}: {r['n']}")
if __name__=="__main__": main()
