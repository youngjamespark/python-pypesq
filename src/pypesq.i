// pypesq.i

%module pypesq

%begin %{
    #define SWIG_FILE_WITH_INIT
%}

// %include "std_string.i"

%{
#include "pypesq.h"
%}

%include "pypesq.h"

