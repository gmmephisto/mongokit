%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%define srcname mongokit

Name:           python-%{srcname}
Version:        0.9.1
Release:        CROC1%{?dist}
Summary:        Python mongodb kit

Group:          Development/Libraries
License:        Apache License 2
URL:            https://github.com/namlook/mongokit
Source0:        %{srcname}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-mongo >= 2.6.3
BuildRequires:  python-nose1.1

Requires:       python-mongo >= 2.6.3
Requires:       mongodb, python-anyjson


%description
MongoKit is a python module that brings structured schema and validation layer
on top of the great pymongo driver. It has be written to be as simple and light
as possible with the KISS and DRY principles in mind.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

find $RPM_BUILD_ROOT/ -name '*.egg-info' -exec rm -rf -- '{}' '+'


## TODO: Tests are need an active mongodb connection
# %check
# nosetests1.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG LICENSE README.md
%{python_sitelib}/*


%changelog
* Tue Jul 15 2014 Mikhail Ushanov <gm.mephisto@gmail.com> 0.9.1-CROC1
- New version

* Sat Sep 17 2011 Pau Aliagas <linuxnow@gmail.com> 0.7.2-1
- Initial version
