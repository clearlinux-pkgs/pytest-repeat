#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-repeat
Version  : 0.6.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/62/52/6fdeac5f3b8ad54d5262b3dadf87e1ef20d76498184f2e8aba612f387c62/pytest-repeat-0.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/52/6fdeac5f3b8ad54d5262b3dadf87e1ef20d76498184f2e8aba612f387c62/pytest-repeat-0.6.0.tar.gz
Summary  : pytest plugin for repeating tests
Group    : Development/Tools
License  : MPL-2.0
Requires: pytest-repeat-python3
Requires: pytest-repeat-license
Requires: pytest-repeat-python
Requires: pytest
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
===================

%package license
Summary: license components for the pytest-repeat package.
Group: Default

%description license
license components for the pytest-repeat package.


%package python
Summary: python components for the pytest-repeat package.
Group: Default
Requires: pytest-repeat-python3

%description python
python components for the pytest-repeat package.


%package python3
Summary: python3 components for the pytest-repeat package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytest-repeat package.


%prep
%setup -q -n pytest-repeat-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533133574
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pytest-repeat
cp LICENSE %{buildroot}/usr/share/doc/pytest-repeat/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/pytest-repeat/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
