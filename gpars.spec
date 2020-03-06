Name:		gpars
Version:	1.2.1
Release:	13
Summary:	Groovy Parallel Systems
License:	ASL 2.0 and Public Domain	
URL:		https://github.com/GPars/GPars
Source0:	https://github.com/GPars/GPars/archive/release-%{version}.tar.gz
Source1:	LICENSE-2.0.txt

Patch0:         0001-JSR-166.patch
Patch1:         0002-Enable-XMvn-local-mode.patch
Patch2:         0003-Port-build-script-to-current-gradle.patch
Patch3:         gpars-1.2.1-port-to-netty-3.10.6.patch

BuildArch:      noarch
BuildRequires:	gradle-local >= 2.1-0.10 apache-parent extra166y
BuildRequires:  jcsp netty3 groovy-lib multiverse

%description
The GPars framework (http://www.gpars.org) offers Java developers 
intuitive and safe ways to handle Java or Groovy tasks concurrently. 
Leveraging the enormous flexibility of the Groovy programing language 
and building on proven Java technologies, we aim to make concurrent 
programming for multi-core hardware intuitive, robust and enjoyable.

%prep
%autosetup -n GPars-release-%{version} -p1

cp %{SOURCE1} .
rm -rf lib/ gradle/wrapper/
rm -rf src/main/groovy/groovyx/gpars/extra166y/

%build
%gradle_build -f

%install
%mvn_install

%files
%doc README.md
%license LICENSE-2.0.txt
%{_datadir}/java/gpars/gpars.jar
%{_datadir}/maven-metadata/gpars.xml

%changelog
* Wed Dec 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-13
- Package init
