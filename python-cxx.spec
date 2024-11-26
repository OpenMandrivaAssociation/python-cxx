#
# this file is based on openSUSE spec file for package python-cxx
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%global module pycxx

%bcond python2	0

Summary:        Write Python extensions in C++
Name:           python-cxx
Version:        7.1.8
Release:        1
License:        BSD
Group:          Development/Python
Url:            https://CXX.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cxx/%{module}-%{version}.tar.gz
Patch0:         %{name}-6.2.3-change-include-paths.patch
BuildRequires:	pkgconfig(python3)
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

#-----------------------------------------------------------------------

%if %{with python2}
%package -n python2-cxx
Summary: Write Python 2.x extensions in C++
Group: Development/Python
BuildRequires: python2-devel

%description -n python2-cxx
PyCXX is a set of classes to help create extensions of Python in the C
language. The first part encapsulates the Python C API taking care of
exceptions and ref counting. The second part supports the building of Python
extension modules in C++.

%files -n python2-cxx
%license COPYRIGHT
%doc README.html
%{py2_puresitedir}/*
%endif

#-----------------------------------------------------------------------

%if %{with python2}
%package -n python2-cxx-devel
Summary:        Python2-cxx Header files
Group:          Development/Python
Requires:       python2-cxx = %{EVRD}
Requires:       python2-devel

%description -n python2-cxx-devel
Header files and documentation for python2-cxx development.

%files -n python2-cxx-devel
%doc Doc/Python2/
%dir %{_datadir}/python2*
%{_includedir}/python2*/CXX
%{_datadir}/python2*/CXX
%endif

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}


mkdir -p PY2
cp -a `ls |grep -v PY2` PY2/

2to3 -w Lib/__init__.py

%build
%py_build

%if %{with python2}
pushd PY2
%py2_build
#python2 setup.py build
popd
%endif

%install
%if %{with python2}
pushd PY2
#PYTHONDONTWRITEBYTECODE=true python2 setup.py install --root=%{buildroot} --prefix="%{_prefix}"
%py2_install
install CXX/*.hxx %{buildroot}/%{_includedir}/python2*/CXX
install CXX/*.h %{buildroot}/%{_includedir}/python2*/CXX/
cp -R CXX/Python2 %{buildroot}/%{_includedir}/python2*/CXX/
#dh_link -ppython-cxx-dev /usr/include/$${i}/CXX/ /usr/include/$${i}_d/CXX; \
install Src/*.c %{buildroot}/%{_datadir}/python2*/CXX/
install Src/*.cxx %{buildroot}/%{_datadir}/python2*/CXX/
cp -R Src/Python2 %{buildroot}/%{_datadir}/python2*/CXX/
chmod -x %{buildroot}/%{_datadir}/python2*/CXX/*.*
chmod -x %{buildroot}/%{_includedir}/python2*/CXX/*.*
popd
%endif

#PYTHONDONTWRITEBYTECODE=true python setup.py install --root=%{buildroot} --prefix="%{_prefix}"
%py_install
install CXX/*.hxx %{buildroot}/%{_includedir}/python3*/CXX
install CXX/*.h %{buildroot}/%{_includedir}/python3*/CXX/
cp -R CXX/Python3 %{buildroot}/%{_includedir}/python3*/CXX/
#dh_link -ppython-cxx-dev /usr/include/$${i}/CXX/ /usr/include/$${i}_d/CXX; \
install Src/*.c %{buildroot}/%{_datadir}/python3*/CXX/
install Src/*.cxx %{buildroot}/%{_datadir}/python3*/CXX/
cp -R Src/Python3 %{buildroot}/%{_datadir}/python3*/CXX/
chmod -x %{buildroot}/%{_datadir}/python3*/CXX/*.*
chmod -x %{buildroot}/%{_includedir}/python3*/CXX/*.*

