#include <iostream>
#include <vector>

using namespace std;

vector<char> blockToRow(vector<vector<char>> sudoku, int rowno, int columnno)
{
  vector<char> row;
  vector<vector<char>> block(3, vector<char>(3));

  int g = rowno - (rowno % 3 );
  int h = columnno - (columnno % 3);
  for (int i=g; i<g+3; i++)
  {
    for (int j=h; j<h+3; j++)
    {
      row.push_back(sudoku[i][j]);
    }
  }
  return row;
}

vector<char> columnToRow(vector<vector<char>> sudoku, int c)
{
  int n = sudoku[0].size();
  vector<char> row(n);
  for (int i=0; i<n; i++)
  {
    row[i]=sudoku[i][c];
  }
  return row;
}

bool isvalidSudokuRow(vector<char> sudokurow)
{
  int n = sudokurow.size();
  vector<char> row(n);

  for (int i=0; i<n; i++)
  {
    for (int j=0; j<n; j++)
    {
      if (sudokurow[i]==row[j])
      {
        return false;
      }
      else if (j==n-1 && sudokurow[i]!=row[j] && sudokurow[i]!='.')
      {
        row[i]=sudokurow[i];
      }
    }
  }
  return true;
}

bool allSudokuRowsValid(vector<vector<char>> sudoku)
{
  int n = sudoku[0].size();
  for (int i=0; i<n; i++)
  {
    if (!isvalidSudokuRow(sudoku[i]))
    {
      return false;
    }
  }
  return true;
}

bool allSudokuColumnsValid(vector<vector<char>> sudoku)
{
  int n = sudoku[0].size();
  for (int i=0; i<n; i++)
  {
    if (!isvalidSudokuRow(columnToRow(sudoku,i)))
    {
      return false;
    }
  }
  return true;
}

bool allSudokuBlocksValid(vector<vector<char>> sudoku)
{
  int n = sudoku[0].size();
  for (int i=0; i<n; i=i+3)
  {
    for (int j=0; j<n; j=j+3)
    {
      if (!isvalidSudokuRow(blockToRow(sudoku,i,j)))
      {
        return false;
      }
    }
  }
  return true;
}

bool checkSudokuCharacters(vector<vector<char>> sudoku)
{
  int n = sudoku[0].size();
  vector<char> validCharacters = {'.','1','2','3','4','5','6','7','8','9'};
  int sudokusize = n*n;
  int validcharcount = 0;

  for (int i=0; i<n; i++)
  {
    for (int j=0; j<n; j++)
    {
      for (int k=0; k<10; k++)
      {
        if (sudoku[i][j]==validCharacters[k])
        {
          validcharcount+=1;
        }
      }
    }
  }
  if (validcharcount==sudokusize)
    return true;
  else
    return false;
}

bool validSudoku(vector<vector<char>> sudoku)
{
  if (allSudokuBlocksValid(sudoku) && allSudokuColumnsValid(sudoku) && allSudokuRowsValid(sudoku) && checkSudokuCharacters(sudoku))
  {
    return true;
  }
  return false;
}
