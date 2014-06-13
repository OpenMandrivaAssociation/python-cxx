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


Name:           python-cxx
Version:        6.2.3
Release:        2
License:        BSD
Summary:        Write Python extensions in C++

Url:            http://CXX.sourceforge.net/
Group:          Development/Python
Source0:        pycxx-%{version}.tar.gz
Patch0:         %{name}-%{version}-change-include-paths.patch
Patch1:         %{name}-%{version}-fix-indentation.patch
BuildRequires:  python-devel
BuildArch:      noarch

%description
PyCXX is a set of classes to help create extensions of Python in the C
language. The first part encapsulates the Python C API taking care of
exceptions and ref counting. The second part supports the building of Python
extension modules in C++.

%package devel
Summary:        Python-cxx Header files

Group:          Development/Python
Requires:       %{name} = %{version}
Requires:       python-devel

%description devel
Header files and documentation for python-cxx development.

%prep
%setup -q -n pycxx-%{version}
%patch0 -p1
%patch1 -p1

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot} --prefix="%{_prefix}"
install CXX/*.hxx %{buildroot}/%{_includedir}/*/CXX
install CXX/*.h %{buildroot}/%{_includedir}/*/CXX/
cp -R CXX/Python2 %{buildroot}/%{_includedir}/*/CXX/
#dh_link -ppython-cxx-dev /usr/include/$${i}/CXX/ /usr/include/$${i}_d/CXX; \
install Src/*.c %{buildroot}/%{_datadir}/*/CXX/
install Src/*.cxx %{buildroot}/%{_datadir}/*/CXX/
cp -R Src/Python2 %{buildroot}/%{_datadir}/*/CXX/
chmod -x %{buildroot}/%{_datadir}/python*/CXX/*.*
chmod -x %{buildroot}/%{_includedir}/python*/CXX/*.*

%files
%doc README.html COPYRIGHT
%{py_puresitedir}/*

%files devel
%doc Doc/Python2/
%dir %{_datadir}/python*
%{_includedir}/python*/CXX
%{_datadir}/python*/CXX
