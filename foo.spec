Summary: foo
Name: foo
Version: 7
Release: 1
License: GPL
Group: Development/Languages
Source: %{name}-%{version}.tar.gz
%description
dummy RPM to get RPM environment variables (BUILD and SRC)

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_ROOT/%{_prefix}
mkdir -p %{buildroot}/%{_prefix}
#install -d -m 755 $RPM_BUILD_ROOT/%{_prefix}
#install -d -m 755 %{buildroot}/%{_prefix}
cp -rf %{_sourcedir}/* %{buildroot}/%{_prefix}/

file=/tmp/rpm_env
[[ -f $file ]] && rm $file
echo '# this file is generated by using rpm -bp rpm_env.spec' >$file
echo RPM_BUILD_DIR=%{_builddir}    >>$file
echo RPM_RPMS_DIR=%{_rpmdir}       >>$file
echo RPM_SOURCES_DIR=%{_sourcedir} >>$file
echo RPM_SPECS_DIR=%{_specdir}     >>$file
echo RPM_SRPMS_DIR=%{_srcrpmdir}   >>$file
echo RPM_DOC_DIR=%{_docdir}        >>$file
echo RPM_TOP_DIR=%{_topdir}        >>$file
echo ARCH=%{_target_cpu}           >>$file
echo PREFIX=%{_prefix}             >>$file
echo TMP=%{_tmppath}               >>$file

%files
%dir %{_prefix}/%{name}-%{version}
%dir %{_prefix}/%{name}-%{version}/rel-eng
%dir %{_prefix}/%{name}-%{version}/src
%dir %{_prefix}/%{name}-%{version}/rel-eng/packages
%dir %{_prefix}/%{name}-%{version}/rel-eng/packages/foo
%dir %{_prefix}/%{name}-%{version}/src/project
%{_prefix}/%{name}-%{version}.tar.gz
%{_prefix}/%{name}-%{version}/rel-eng/tito.props
%{_prefix}/%{name}-%{version}/rel-eng/packages/.readme
%{_prefix}/%{name}-%{version}/rel-eng/packages/foo
%{_prefix}/%{name}-%{version}/src/project/hello.txt
%{_prefix}/%{name}-%{version}/foo.spec
%{_prefix}/%{name}-%{version}/.gitignore
