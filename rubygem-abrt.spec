# Generated from abrt-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name abrt

# There are not all test dependencies are available in RHEL.
%global enable_test 0%{!?rhel:1}

Summary: ABRT support for Ruby MRI
Name: rubygem-%{gem_name}
Version: 0.0.6
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/voxik/abrt-ruby
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/voxik/abrt-ruby.git && cd abrt-ruby && git checkout v0.0.6
# tar czvf abrt-0.0.6-specs.tar.gz spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: libreport-filesystem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{enable_test} > 0
BuildRequires: rubygem(rspec)
%endif
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Provides ABRT reporting support for applications written using Ruby.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_sysconfdir}/libreport/events.d/
cp -a .%{gem_instdir}/config/ruby_event.conf %{buildroot}%{_sysconfdir}/libreport/events.d/

%if %{enable_test} > 0
%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}

rspec spec

popd
%endif


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%exclude %{gem_instdir}/config
%config(noreplace) %{_sysconfdir}/libreport/events.d/ruby_event.conf

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Oct 24 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.6-1
- Update to abrt 0.0.6.
  - Resolves: rhbz#1021872

* Tue Jul 02 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.5-2
- Disable tests for EL builds.

* Mon May 06 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.5-1
- Update to abrt 0.0.5.

* Mon Mar 04 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.3-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 17 2012 Vít Ondruch <vondruch@redhat.com> - 0.0.3-1
- Update to abrt 0.0.3.

* Mon Jul 09 2012 Vít Ondruch <vondruch@redhat.com> - 0.0.2-1
- Initial package
