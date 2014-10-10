%define upstream_name    Perl6-Doc
%define upstream_version 0.47

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl 6 Documentation Collection
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl6/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::ShareDir::Install)
BuildArch:	noarch

%description
This Perl module distribution contains all the latest Perl 6 documentation
and a utility called 'p6doc' for viewing it.

Below is the list of documents that are currently available; a number in
the column indicates, the document is currently available. An asterisk next
to a number means that the document is an unofficial draft written by a
member of the Perl community but not approved by the Perl 6 Design Team.
The pages after the first section are anyway no Design docs.

Contents
        S01  The Ugly, the Bad, and the Good   (A01)
        S02  Bits and Pieces                   (A02) (E02)
        S03  Operators                         (A03) (E03)
        S04  Syntax                            (A04) (E04)
        S05  Pattern Matching                  (A05) (E05)
        S06  Subroutines                       (A06) (E06)
             Formats                                 (E07)
        S09  Data Structures
        S10  Packages
        S11  Modules
        S12  Objects                           (A12)
        S13  Overloading
        S16* IPC / IO / Signals  
        S17* Concurrency
             Debugging                         (A20*)
        S22* CPAN
             Portable Perl
        S26  Perl Documentation
        S27* Perl Culture
        S28* Special Names
        S29  Functions
    
        F01  FAQ::Captures
        F02  FAQ::FUD
    
        O01  Overview
        O03  Overview::Operator
        O04  Overview::Smartmatch
        O05  Overview::Reduce
        O07  Overview::Variable
        O08  Overview::Data
        O10  Overview::File
        O12  Overview::Functions
        O14  Overview::Control
        O15  Overview::Subroutine
        O17  Overview::Object
        O20  Overview::Rule
    
        T01  Tutorial perlintro
    
        M01  Report on the Perl 6 Announcement
        M02  What is Perl 6 ?
        M03  A Plan for Pugs
        M04  Everyday Perl 6
        M05  Yet Another Perl 6 Operator (Microarticles)
        M06  The Beauty of Perl 6 Parameter Passing

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.470.0-2mdv2011.0
+ Revision: 657823
- rebuild for updated spec-helper

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.470.0-1mdv2011.0
+ Revision: 612344
- update to new version 0.47

  + Jérôme Quelin <jquelin@mandriva.org>
    - update to 0.45

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.450.0-1mdv2010.0
+ Revision: 418116
- update to 0.45

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2010.0
+ Revision: 399596
- update to 0.43

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2010.0
+ Revision: 396745
- update to 0.41

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.0
+ Revision: 396310
- update to 0.40

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.0
+ Revision: 396308
- import perl-Perl6-Doc


* Wed Jul 15 2009 cpan2dist 0.36-1mdv
- initial mdv release, generated with cpan2dist
