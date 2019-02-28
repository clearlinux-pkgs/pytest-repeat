#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-repeat
Version  : 0.8.0
Release  : 12
URL      : https://files.pythonhosted.org/packages/1a/ef/a721646e592e834ad93e1c880956b3d6ff060c623c2e317170f5747d9c71/pytest-repeat-0.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1a/ef/a721646e592e834ad93e1c880956b3d6ff060c623c2e317170f5747d9c71/pytest-repeat-0.8.0.tar.gz
Summary  : pytest plugin for repeating tests
Group    : Development/Tools
License  : License-2.0(MPL-2.0) MPL-2.0 Mozilla
Requires: pytest-repeat-license = %{version}-%{release}
Requires: pytest-repeat-python = %{version}-%{release}
Requires: pytest-repeat-python3 = %{version}-%{release}
Requires: pytest
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
pytest-repeat
===================
pytest-repeat is a plugin for `py.test <https://docs.pytest.org>`_ that makes it
easy to repeat a single test, or multiple tests, a specific number of times.

%package license
Summary: license components for the pytest-repeat package.
Group: Default

%description license
license components for the pytest-repeat package.


%package python
Summary: python components for the pytest-repeat package.
Group: Default
Requires: pytest-repeat-python3 = %{version}-%{release}

%description python
python components for the pytest-repeat package.


%package python3
Summary: python3 components for the pytest-repeat package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytest-repeat package.


%prep
%setup -q -n pytest-repeat-0.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551396915
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-repeat
cp LICENSE %{buildroot}/usr/share/package-licenses/pytest-repeat/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-repeat/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
