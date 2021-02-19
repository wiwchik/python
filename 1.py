import csv
import pandas as pd
from pandas import DataFrame
from prettytable import PrettyTable


def f1(rest):
    for m in range(1, len(rest)):
        if rest[m - 1][7] == rest[m][7]:
            if rest[m - 1][6] < rest[m][6] and rest[m - 1][6] != rest[m][6]:
                rest[m - 1][0], rest[m][0] = rest[m][0], rest[m - 1][0]
            elif rest[m - 1][6] == rest[m][6]:
                if rest[m - 1][3] < rest[m][3] and rest[m - 1][3] != rest[m][3]:
                    rest[m - 1][0], rest[m][0] = rest[m][0], rest[m - 1][0]
                elif rest[m - 1][3] == rest[m][3]:
                    rest[m - 1][0] = rest[m][0]
    rest = sorted(rest, key=lambda p: p[0])
    return rest


def f(team, DataFrame):
    res = []
    GamesTotal = 0
    Wins = 0
    Draws = 0
    Losses = 0
    Scored = 0
    Conceded = 0
    GoalDiff = 0
    Points = 0
    s = df.shape[0]
    for j in range(s):
        if DataFrame.HomeTeam[j] == team:
            GamesTotal = GamesTotal + 1
            Scored = Scored + DataFrame.FTHG[j]
            Conceded = Conceded + DataFrame.FTAG[j]
            if DataFrame.FTHG[j] > DataFrame.FTAG[j]:
                Wins = Wins + 1
                Points = Points + 3
            elif DataFrame.FTHG[j] == DataFrame.FTAG[j]:
                Draws = Draws + 1
                Points = Points + 1
        elif DataFrame.AwayTeam[j] == team:
            GamesTotal = GamesTotal + 1
            Scored = Scored + DataFrame.FTAG[j]
            Conceded = Conceded + DataFrame.FTHG[j]
            if DataFrame.FTHG[j] < DataFrame.FTAG[j]:
                Wins = Wins + 1
                Points = Points + 3
            elif DataFrame.FTHG[j] == DataFrame.FTAG[j]:
                Draws = Draws + 1
                Points = Points + 1
    Losses = GamesTotal - Wins - Draws
    GoalDiff = Scored - Conceded
    res.append(GamesTotal)
    res.append(Wins)
    res.append(Draws)
    res.append(Losses)
    res.append(GoalDiff)
    res.append(Points)
    return res


def all_m_team(t, DataFrame):
    s = df1.shape[0]
    x = PrettyTable()
    x.field_names = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
    for q in range(s):
        if DataFrame.HomeTeam[q] == t or DataFrame.AwayTeam[q] == t:
            x.add_row([DataFrame.Date[q], DataFrame.HomeTeam[q],
                      DataFrame.AwayTeam[q], DataFrame.FTHG[q],
                      DataFrame.FTAG[q]])
    print(x)


def date_m(dt, DataFrame):
    s = df2.shape[0]
    x = PrettyTable()
    x.field_names = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
    for q in range(s):
        if DataFrame.Date[q] == dt:
            x.add_row([DataFrame.Date[q], DataFrame.HomeTeam[q],
                       DataFrame.AwayTeam[q], DataFrame.FTHG[q],
                       DataFrame.FTAG[q]])
    print(x)


ur = input('What do you want?\n'
           '                \nA - Show all matches of a given team\n'
           '                \nB - Show matches played on a given date\n'
           '                \nC - Show the ranking table\n'
           '                ')
if ur == 'A':
    df1 = pd.read_csv('SP1.csv')  # ВОТ
    t = input('Team name: ')
    t = t.title()
    all_m_team(t, df1)
if ur == 'B':
    df2 = pd.read_csv('SP1.csv')
    dt = input('Date in DD/MM/YYYY format: ')
    date_m(dt, df2)
if ur == 'C':
    df = pd.read_csv('SP1.csv')
    row = []
    rest = []
    k = 0
    Teams = []
    for i in df.HomeTeam:
        if i not in Teams:
            Teams.append(i)

    for i in Teams:
        row = (f(i, df))
        row.insert(0, i)
        rest.append(row)

    rest = sorted(rest, key=lambda p: p[6], reverse=True)

    a = 1
    for i in range(len(rest)):
        rest[i].insert(0, a)
        a = a + 1

    for b in range(1, len(rest)):
        if rest[b - 1][7] == rest[b][7]:
            rest1 = f1(rest)
            break

    x = PrettyTable()
    x.field_names = ['Place', 'Team Name', 'Games', 'W', 'D', 'L', 'GD', 'Points']
    for el in rest1:
        x.add_row(el)
    print(x)
