% --- Database ---
% student(Name, RollNo).
student('Sabiha', 101).
student('Rahul', 102).
student('Anjali', 103).
student('Arjun', 104).

% teacher(Name, EmpId).
teacher('Dr. Kumar', t01).
teacher('Dr. Meena', t02).
teacher('Prof. Ramesh', t03).

% subject(SubCode, SubName, TeacherId).
subject('CS101', 'Artificial Intelligence', t01).
subject('CS102', 'Data Structures', t02).
subject('CS103', 'Databases', t03).

% enrolled(StudentRoll, SubCode).
enrolled(101, 'CS101').
enrolled(101, 'CS102').
enrolled(102, 'CS102').
enrolled(103, 'CS103').
enrolled(104, 'CS101').
enrolled(104, 'CS103').

% --- Rules ---
% Find which subject a student is enrolled in
student_subject(StudentName, SubName) :-
    student(StudentName, RollNo),
    enrolled(RollNo, SubCode),
    subject(SubCode, SubName, _).

% Find teacher of a subject
subject_teacher(SubName, TeacherName) :-
    subject(_, SubName, TId),
    teacher(TeacherName, TId).

% Find teacher of a student
student_teacher(StudentName, TeacherName) :-
    student_subject(StudentName, SubName),
    subject_teacher(SubName, TeacherName).
