!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!
!	RMG - Reaction Mechanism Generator
!
!	Copyright (c) 2002-2009 Prof. William H. Green (whgreen@mit.edu) and the
!	RMG Team (rmg_dev@mit.edu)
!
! 	Permission is hereby granted, free of charge, to any person obtaining a
! 	copy of this software and associated documentation files (the 'Software'),
! 	to deal in the Software without restriction, including without limitation
! 	the rights to use, copy, modify, merge, publish, distribute, sublicense,
! 	and/or sell copies of the Software, and to permit persons to whom the
! 	Software is furnished to do so, subject to the following conditions:
!
! 	The above copyright notice and this permission notice shall be included in
! 	all copies or substantial portions of the Software.
!
! 	THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
! 	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
! 	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
! 	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
! 	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
! 	FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
! 	DEALINGS IN THE SOFTWARE.
!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

! Items placed in this module will be exposed to Python.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

module params

	implicit none

	integer :: nT
	real(8), dimension(:), pointer :: Tlist
	real(8), dimension(:), pointer :: Cvlist

	integer :: mcon
	integer :: mequa
	integer :: nvars

	integer :: nvib
	integer :: nrot

	real(8) :: nu_low
	real(8) :: nu_mid
	real(8) :: nu_high

contains

	subroutine setParams(p_nT, p_Tlist, p_Cvlist, p_mcon, p_mequa, p_nvars, &
		p_nvib, p_nrot, p_nu_low, p_nu_mid, p_nu_high)
		! Set the module parameters based on the values in the parameter list.

		integer, intent(in) :: p_nT								! The number of temperatures at which Cv data is given
		real(8), dimension(1:p_nT), intent(in) :: p_Tlist		! The list of temperatures in K at which Cv data is given
		real(8), dimension(1:p_nT), intent(in) :: p_Cvlist		! The list of heat capacity data (dimensionless) at each temperature
		integer, intent(in) :: p_mcon
		integer, intent(in) :: p_mequa
		integer, intent(in) :: p_nvars							! The number of variables used in the fitting
		integer, intent(in) :: p_nvib							! The number of harmonic oscillators to fit
		integer, intent(in) :: p_nrot							! The number of hindered rotors to fit
		real(8), intent(in) :: p_nu_low
		real(8), intent(in) :: p_nu_mid
		real(8), intent(in) :: p_nu_high
		
		nT = p_nT
		allocate( Tlist(1:nT), Cvlist(1:nT) )
		Tlist = p_Tlist
		Cvlist = p_Cvlist

		mcon = p_mcon
		mequa = p_mequa
		nvars = p_nvars
		
		nvib = p_nvib
		nrot = p_nrot

		nu_low = p_nu_low
		nu_mid = p_nu_mid
		nu_high = p_nu_high

	end subroutine
	
	subroutine cleanup()
		! Clean up arrays allocated when setting up the module parameters.
	
		deallocate( Tlist, Cvlist )
		
	end subroutine

end module

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

subroutine fitModes(x0, nx, bl, bu, ind, maxiter, xout, igo)
	! Execute a constrained nonlinear optimization to fit molecular degrees of
	! freedom to heat capacity data.

	use params
	implicit none

	integer, intent(in) :: nx
	real(8), dimension(1:nx), intent(in) :: x0			! The initial guess to the solver for each variable
	real(8), dimension(1:nx), intent(in) :: bl			! The lower bounds for each variable
	real(8), dimension(1:nx), intent(in) :: bu			! The lower bounds for each variable
	integer, dimension(1:nx), intent(in) :: ind			! The type of bounds for each variable
	integer, intent(in) :: maxiter						! The maximum number of iterations to try
	real(8), dimension(1:nx), intent(out) :: xout		! The returned solution vector
	integer, intent(out) :: igo							! The returned solution status

	real(8), dimension(1:nx) :: x

	external caseDirect
	external caseNvibNrot

	! These variables are required by the nonlinear solver
	integer, parameter :: lwork = 785
	integer, parameter :: liwork = 103
	real(8) :: fj(nT,nvars+1)
	real(8) :: fnorm
	integer :: iopt(24)
	integer :: iwork(liwork)
	real(8) :: ropt(1)
	real(8) :: work(lwork)
	integer :: ldfj

	ldfj = mcon + mequa

	! Tell how much storage we gave the solver
	iwork(1) = lwork
	iwork(2) = liwork

	! Additional solver options
	iopt(1)=4         ! Set the option to change the value of TOLF
	iopt(2)=1         ! Where in ROPT to look for the new value
	ropt(1)=1.E-9     ! New value for TOLF
	iopt(3)=2         ! Change the number of interations
	iopt(4)=maxiter   ! Maximum number of iterations
	iopt(5)=17        ! Do not allow the flag IGO to return the value IGO=3
	iopt(6)=1         ! Forces a full model step
	iopt(7)=99        ! No further options are changed

	! x is used to store the input to dqed and is overwritten with the output
	! from dqed, so it needs to be a temporary variable
	x = x0

	! Execute the optimization
	! We use a different helper function based on the number of oscillators
	! and rotors we are trying to fit
	if (nvib + 2 * nrot < nT) then
		call dqed(caseDirect, mequa, nvars, mcon, ind, bl, bu, &
			x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
	else
		call dqed(caseNvibNrot, mequa, nvars, mcon, ind, bl, bu, &
			x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
	end if
!	if (nrot == 0) then
!		if (nvib == 0) then
!
!		elseif (nvib == 1) then
!			call dqed(case1vib0rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 2) then
!			call dqed(case2vib0rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 3) then
!			call dqed(case3vib0rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 4) then
!			call dqed(case4vib0rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 5) then
!			call dqed(case5vib0rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 6) then
!			call dqed(case6vib0rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib >= 7) then
!			call dqed(caseNvib0rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		end if
!	elseif (nrot == 1) then
!		if (nvib == 0) then
!			call dqed(case0vib1rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 1) then
!			call dqed(case1vib1rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 2) then
!			call dqed(case2vib1rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 3) then
!			call dqed(case3vib1rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 4) then
!			call dqed(case4vib1rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib >= 5) then
!			call dqed(caseNvib1rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		end if
!	elseif (nrot == 2) then
!		if (nvib == 0) then
!			call dqed(case0vib2rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 1) then
!			call dqed(case1vib2rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 2) then
!			call dqed(case2vib2rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 3) then
!			call dqed(case3vib2rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib >= 4) then
!			call dqed(caseNvib2rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		end if
!	elseif (nrot == 3) then
!		if (nvib == 0) then
!			call dqed(case0vib3rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 1) then
!			call dqed(case1vib3rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 2) then
!			call dqed(case2vib3rot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 3) then
!			call dqed(case3vibNrot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib >= 4) then
!			call dqed(caseNvibNrot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		end if
!	elseif (nrot >= 4) then
!		if (nvib == 0) then
!			call dqed(case0vibNrot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 1) then
!			call dqed(case1vibNrot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 2) then
!			call dqed(case2vibNrot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib == 3) then
!			call dqed(case3vibNrot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		elseif (nvib >= 4) then
!			call dqed(caseNvibNrot, mequa, nvars, mcon, ind, bl, bu, &
!				x, fj, ldfj, fnorm, igo, iopt, ropt, iwork, work)
!		end if
!	end if

	! Store the results in the output vector
	! We defer interpreting them until after returning to Python
	xout = x

end subroutine

