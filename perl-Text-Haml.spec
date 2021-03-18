#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Haml
Version  : 0.990118
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/V/VT/VTI/Text-Haml-0.990118.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/V/VT/VTI/Text-Haml-0.990118.tar.gz
Summary  : 'Haml Perl implementation'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Text-Haml-license = %{version}-%{release}
Requires: perl-Text-Haml-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
# NAME
Text::Haml - Haml Perl implementation
# SYNOPSIS
use Text::Haml;
my $haml = Text::Haml->new;

%package dev
Summary: dev components for the perl-Text-Haml package.
Group: Development
Provides: perl-Text-Haml-devel = %{version}-%{release}
Requires: perl-Text-Haml = %{version}-%{release}

%description dev
dev components for the perl-Text-Haml package.


%package license
Summary: license components for the perl-Text-Haml package.
Group: Default

%description license
license components for the perl-Text-Haml package.


%package perl
Summary: perl components for the perl-Text-Haml package.
Group: Default
Requires: perl-Text-Haml = %{version}-%{release}

%description perl
perl components for the perl-Text-Haml package.


%prep
%setup -q -n Text-Haml-0.990118
cd %{_builddir}/Text-Haml-0.990118

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Haml
cp %{_builddir}/Text-Haml-0.990118/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Haml/d0d70d43f22d9ba44a7f5a48a6c5925165062974
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Haml.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Haml/d0d70d43f22d9ba44a7f5a48a6c5925165062974

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Text/Haml.pm
