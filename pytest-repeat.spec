#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-repeat
Version  : 0.9.1
Release  : 39
URL      : https://files.pythonhosted.org/packages/1e/69/f7411070a07bc8949725b57d9298ac445e59edb26e3b74b4f97d52afe47a/pytest-repeat-0.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/1e/69/f7411070a07bc8949725b57d9298ac445e59edb26e3b74b4f97d52afe47a/pytest-repeat-0.9.1.tar.gz
Summary  : pytest plugin for repeating tests
Group    : Development/Tools
License  : MPL-2.0
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
===================

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
Provides: pypi(pytest_repeat)
Requires: pypi(pytest)

%description python3
python3 components for the pytest-repeat package.


%prep
%setup -q -n pytest-repeat-0.9.1
cd %{_builddir}/pytest-repeat-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604339500
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-repeat
cp %{_builddir}/pytest-repeat-0.9.1/LICENSE %{buildroot}/usr/share/package-licenses/pytest-repeat/50953f9d37c2d40da546a6cadfbf93210410f06f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-repeat/50953f9d37c2d40da546a6cadfbf93210410f06f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
