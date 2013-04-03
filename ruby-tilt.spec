%define		bootstrap 1
%define		module	tilt
Summary:	Generic interface to multiple Ruby template engines
Name:		ruby-%{module}
Version:	1.3.5
Release:	0.1
License:	MIT
Group:		Development/Languages
URL:		http://github.com/rtomayko/%{module}
Source0:	http://rubygems.org/gems/%{module}-%{version}.gem
# Source0-md5:	5b72b19fda8a1ec385c89a21eaf5a082
BuildRequires:	ruby
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic interface to multiple Ruby template engines

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -qcT
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.md -o -print | xargs touch --reference %{SOURCE0}

%build
%if %{with tests}
LANG=en_US.utf8 testrb -Ilib test/*_test.rb
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{_bindir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md COPYING HACKING TEMPLATES.md
%attr(755,root,root) %{_bindir}/tilt
%{ruby_rubylibdir}/%{module}.rb
%{ruby_rubylibdir}/%{module}

%if 0
%files doc
%defattr(644,root,root,755)
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/HACKING
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%endif
