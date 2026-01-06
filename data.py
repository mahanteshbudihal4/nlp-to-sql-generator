import pandas as pd

data = {
    "nlp": [
        "show all students","list all students","display all students",
        "give me all students","show students list",

        "students older than 18","students age greater than 18",
        "students whose age is above 18","students with age more than 18",
        "students age above 18",

        "students younger than 18","students age below 18",
        "students age less than 18","students whose age is under 18",
        "students age under 18",

        "students exactly 18 years old","students age equals 18",
        "students with age 18","students whose age is 18","students age is 18",

        "how many students are there","count students",
        "total number of students","number of students","count all students",

        "show students ordered by age","list students sorted by age",
        "students order by age","students sorted by age",

        "show top 5 students","list first 3 students",
        "get 2 students","show top 10 students"
    ],

    "sql": [
        "SELECT * FROM students ;","SELECT * FROM students ;",
        "SELECT * FROM students ;","SELECT * FROM students ;",
        "SELECT * FROM students ;",

        "SELECT * FROM students WHERE age > 18 ;",
        "SELECT * FROM students WHERE age > 18 ;",
        "SELECT * FROM students WHERE age > 18 ;",
        "SELECT * FROM students WHERE age > 18 ;",
        "SELECT * FROM students WHERE age > 18 ;",

        "SELECT * FROM students WHERE age < 18 ;",
        "SELECT * FROM students WHERE age < 18 ;",
        "SELECT * FROM students WHERE age < 18 ;",
        "SELECT * FROM students WHERE age < 18 ;",
        "SELECT * FROM students WHERE age < 18 ;",

        "SELECT * FROM students WHERE age = 18 ;",
        "SELECT * FROM students WHERE age = 18 ;",
        "SELECT * FROM students WHERE age = 18 ;",
        "SELECT * FROM students WHERE age = 18 ;",
        "SELECT * FROM students WHERE age = 18 ;",

        "SELECT COUNT ( * ) FROM students ;",
        "SELECT COUNT ( * ) FROM students ;",
        "SELECT COUNT ( * ) FROM students ;",
        "SELECT COUNT ( * ) FROM students ;",
        "SELECT COUNT ( * ) FROM students ;",

        "SELECT * FROM students ORDER BY age ;",
        "SELECT * FROM students ORDER BY age ;",
        "SELECT * FROM students ORDER BY age ;",
        "SELECT * FROM students ORDER BY age ;",

        "SELECT * FROM students LIMIT 5 ;",
        "SELECT * FROM students LIMIT 3 ;",
        "SELECT * FROM students LIMIT 2 ;",
        "SELECT * FROM students LIMIT 10 ;"
    ]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
print("Dataset created")
