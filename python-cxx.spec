%global module pycxx

Summary:        Write Python extensions in C++
Name:           python-cxx
Version:        7.2.0
Release:        2
License:        BSD
Group:          Development/Python
Url:            https://CXX.sourceforge.net/
# 465 is tagged as 7.2.0, but the release hasn't been uploaded to the files area
Source0:        https://sourceforge.net/code-snapshots/svn/c/cx/cxx/code/cxx-code-r465-trunk.zip
Patch0:         %{name}-6.2.3-change-include-paths.patch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

BuildArch:      noarch

%description
PyCXX is a set of classes to help create extensions of Python in the C
language. The first part encapsulates the Python C API taking care of
exceptions and ref counting. The second part supports the building of Python
extension modules in C++.

%files
%license COPYRIGHT
%doc README.html
%{py_puresitedir}/*


#-----------------------------------------------------------------------

%package devel
Summary:        Python-cxx Header files
Group:          Development/Python
Requires:       %{name} = %{EVRD}
Requires:       python-devel

%description devel
Header files and documentation for python-cxx development.

%files devel
%doc Doc/Python3/
%dir %{_datadir}/python3*
%{_includedir}/python3*/CXX
%{_datadir}/python3*/CXX


%prep
%autosetup -p1 -n cxx-code-r465-trunk/CXX
