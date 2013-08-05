\ProvidesClass{maclasse}[2007/09/19 Classe personnelle, V1.0]

\LoadClass[a4paper,11pt]{article}

\RequirePackage[
  top=1.42cm, % top margin
  left=1.42cm, % left margin
  textwidth=18.161cm,
  textheight=20.0103cm,
  includehead, % the header is included in the computations
  headheight=3.0138cm, % height of the header
  headsep=26.144882pt,
  heightrounded, % to have an integer number of lines
]{geometry}
\RequirePackage{fontspec}
\setmonofont[Path=../fonts/propcouriersans/]{PropCourierSans-Regular.ttf}
\RequirePackage{lastpage}
\RequirePackage{multicol}
\RequirePackage{array}
\RequirePackage{fancyhdr}
\RequirePackage{graphicx}
\RequirePackage{setspace}
\setstretch{1.272727272727272727} % for custom spacing

% Pages styles
\setlength\parindent{0pt}
\setlength{\parskip}{14pt}
\setlength{\columnsep}{14pt}
\setlength{\tabcolsep}{7pt}

% Header and footer
\pagestyle{fancy}

\newcommand{\foo}{%
    \dimexpr\textwidth/2-\tabcolsep
}

\newcommand{\headertext}{%
    \tt \fontsize{10.5}{14}\selectfont 
    \setstretch{1.272727272727272727} % for custom spacing
    From: Antoon Bosselaers\newline
    Research Applied Cryptography\newline
    antoon.bosselaers@esat.kuleuven.ac.be\newline
    Tel +32 16 32 18 07 — Fax +32 16 32 19 69
}

% Header
\fancyhead{} % clear all header fields
\fancyhead[LE,LO]{
    \begin{tabular}{@{}p{\foo}p{\foo}@{}}
        \vspace*{-10.7mm}
        \hspace*{-9.1mm}
        \includegraphics[height=39.138mm,width=31.397mm]{logo.eps}
        & \headertext
    \end{tabular}
}
\renewcommand{\headrulewidth}{0pt} % no line in header area

% Footer
\fancyfoot{} % clear all footer fields
\fancyfoot[LE,LO]{
    \tt \fontsize{10.5}{14}\selectfont
    \setstretch{1.272727272727272727} % for custom spacing
    \includegraphics[width=15.462mm,height=4.826mm]{kuleuvenlogo.eps}\\
    ESAT/COSIC — Research Applied Cryptography\\
    Kasteelpark Arenberg 10, bus 2446, B3001 Heverlee, Belgium\\
    +32 (0) 16 32 18 07 — http://cosic.esat.kuleuven.be/
    \hspace{3cm}\thepage/\pageref{LastPage}
}

% Signature
\newcommand{\signature}[1] {
    \hspace{92,652 mm}\parbox{87,713mm}{#1}
}

% Date + Subject
\newcommand{\datesubject}[2] {
    #1\\
    {\tt Subject:} #2
}

% Recipient
\newcommand{\recipient}[1] {
    \begin{multicols}{2}
    \hfill\vfill
    \columnbreak
    {
    \tt \fontsize{10.5}{14}
    To: #1 \\\\
    }
    \end{multicols}
}
